from pydantic import BaseModel, Field


class InputModel(BaseModel):
    age: float = Field(..., ge=29.0, le=77.0, description="Age in years")
    sex: int = Field(..., ge=0, le=1, description="Sex (0 = female, 1 = male)")
    cp: float = Field(..., ge=0.0, le=3.0, description="Chest pain type")
    trestbps: float = Field(..., ge=94.0, le=200.0, description="Resting blood pressure (mm Hg)")
    chol: float = Field(..., ge=126.0, le=564.0, description="Serum cholesterol (mg/dl)")
    fbs: int = Field(..., ge=0, le=1, description="Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)")
    restecg: float = Field(..., ge=0.0, le=2.0, description="Resting electrocardiographic results")
    thalach: float = Field(..., ge=71.0, le=202.0, description="Maximum heart rate achieved")
    exang: int = Field(..., ge=0, le=1, description="Exercise induced angina (1 = yes, 0 = no)")
    oldpeak: float = Field(..., ge=0.0, le=6.2, description="ST depression induced by exercise relative to rest")
    slope: float = Field(..., ge=0.0, le=2.0, description="Slope of the peak exercise ST segment")
    ca: float = Field(..., ge=0.0, le=4.0, description="Number of major vessels colored by fluoroscopy")
    thal: float = Field(..., ge=0.0, le=3.0, description="Thalassemia (3 = normal, 6 = fixed defect, 7 = reversable defect)")

    class Config:
        extra = "forbid"