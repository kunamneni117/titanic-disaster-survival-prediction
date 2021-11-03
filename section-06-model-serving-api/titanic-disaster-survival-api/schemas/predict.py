from typing import Any, List, Optional

from pydantic import BaseModel
from classification_model.processing.validation import TitanicDisasterSurvivalDataInputSchema

class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]

class MultipleTitanicDisasterSurvivalDataInputs(BaseModel):
    inputs: List[TitanicDisasterSurvivalDataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "MSSubClass": 20,
                        "MSZoning": "RH",
                        "PassengerId" : 892,
                        "Pclass": 3,
                        "Name": "Kelly, Mr. James",
                        "Sex": "male",
                        "Age": 37,
                        "SibSp": 0,
                        "Parch": 0,
                        "Ticket": "330911",
                        "Fare": "7.8292",
                        "Cabin": None,
                        "Embarked": "Q"
                    }
                ]
            }
        }