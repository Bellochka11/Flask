from fastapi import FastAPI, Path, Query

# uvicorn lec_5.task_3:app --reload   запуск приложения из папки Flask app в 4 строке
app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_item(item_id: int = Path(..., ge=1)): #..., - ПОЛЕ ОБЯЗАТЕЛЬНОЕ ge=1 - ID БОЛЬШЕ ИЛИ РАВНО 1
#     return {"item_id": item_id}


@app.get("/items/{item_id}")
async def read_item(item_id: int = Path(..., title="The ID of the item"), q: str = None):
    return {"item_id": item_id, "q": q}

# @app.get("/items/")
# async def read_items(q: str = Query(None, min_length=3, max_length=50)): # None - ЗНАЧЕНИЕ ПО УМОЛЧАНИЮ
#     results = {"items": [{"item_id": "Spam"}, {"item_id": "Eggs"}]}
#     if q: #ЕСЛИ ПЕРЕДАЛИ ЭТОТ ПАРАМЕТР
#         results.update({"q": q}) # ДОБАВЬ Q В  results
#     return results

@app.get("/items/")
async def read_items(q: str = Query(..., min_length=3, max_length=50)): # None - ЗНАЧЕНИЕ ПО УМОЛЧАНИЮ
    results = {"items": [{"item_id": "Spam"}, {"item_id": "Eggs"}]}
    if q: #ЕСЛИ ПЕРЕДАЛИ ЭТОТ ПАРАМЕТР
        results.update({"q": q}) # ДОБАВЬ Q В  results
    return results