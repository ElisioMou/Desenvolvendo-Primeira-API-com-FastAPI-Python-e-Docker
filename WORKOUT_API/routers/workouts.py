from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/workouts", tags=["Workouts"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Workout])
def list_workouts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_workouts(db, skip=skip, limit=limit)

@router.post("/", response_model=schemas.Workout)
def create_new_workout(workout: schemas.WorkoutCreate, db: Session = Depends(get_db)):
    return crud.create_workout(db, workout)

@router.get("/{workout_id}", response_model=schemas.Workout)
def read_workout(workout_id: int, db: Session = Depends(get_db)):
    db_workout = crud.get_workout(db, workout_id)
    if not db_workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    return db_workout

@router.delete("/{workout_id}", response_model=schemas.Workout)
def delete_workout(workout_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_workout(db, workout_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Workout not found")
    return deleted
