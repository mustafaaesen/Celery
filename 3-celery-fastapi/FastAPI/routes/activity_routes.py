from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from services.activity_service import list_activities
from schemas.activity_schemas import UserActivity

router = APIRouter()

#aktivi kayıtlarının route ının yazılması

#service içinde activity yazıp api üzerinden haberleşmek için yazılır

@router.get("/",response_model=list[UserActivity])
def list_activites_endpoint(db: Session=Depends(get_db)):

    return list_activities(db)  #activitielerin tamamının dönecepi endpoint



