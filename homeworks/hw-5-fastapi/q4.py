import pickle
from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()
input_file = "model2.bin"
dv_file = "dv.bin"

with open(input_file, "rb") as f_in:
    model = pickle.load(f_in)
with open(dv_file, "rb") as f_in:
    dv = pickle.load(f_in)


class CustomerData(BaseModel):
    job: str
    duration: int
    poutcome: str


@app.post("/predict")
async def predict(customer: CustomerData):
    customer_dict = customer.model_dump()
    X = dv.transform([customer_dict])
    y_pred = model.predict_proba(X)[0, 1]
    return {"subscription probability": round(y_pred, 3)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9671)
