from fastapi import FastAPI, Request, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from prometheus_client import Counter, Histogram, Gauge, make_asgi_app
import prometheus_client
import random
import time


app = FastAPI()
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

http_requests_total = Counter(
    "http_requests_total", 
    "Number of HTTP requests received", 
    ["method", "endpoint"]
)

http_requests_milliseconds = Histogram(
    "http_requests_milliseconds",
    "Duration of HTTP requests in milliseconds",
    ["method", "endpoint"]
)

last_sum1n = Gauge("last_sum1n", "Value stores last result of sum1n")
last_fibo = Gauge("last_fibo", "Value stores last result of fibo")
list_size = Gauge("list_size", "Value stores current list size")
last_calculator = Gauge("last_calculator", "Value stores last result of calculator")
errors_calculator_total = Counter(
    "errors_calculator_total",
    "Number of errors in calculator",
    ["error_type"]
)

class CustomValidationError(Exception):

    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

@app.middleware("http")
async def track_requests(request: Request, call_next):
    method = request.method
    endpoint = request.url.path
    http_requests_total.labels(method=method, endpoint=endpoint).inc()

    start_time = time.time()
    response = await call_next(request)
    duration = (time.time() - start_time) * 1000  # перевод в миллисекунды
    http_requests_milliseconds.labels(method=method, endpoint=endpoint).observe(duration)

    return response

# # Exporter
# @app.get("/metrics")
# def metrics():
#     return prometheus_client.generate_latest()


# sum1n handler body ------------------------------------------------------
@app.get("/sum1n/{n}")
def summorial(n: int = Path(ge=0)):
    result = sum([i for i in range(1, n + 1)])
    last_sum1n.set(result)  # обновление метрики с последним результатом
    return {"result": result}
# -------------------------------------------------------------------------


# fibonacci handler body --------------------------------------------------
@app.get("/fibo")
def fibonnaci(n: int = Query(ge=1)):
    if n <= 1:
        return {"result": 0}
    
    prev, current = 0, 1
    for i in range(2, n):
        current, prev = prev + current, current

    last_fibo.set(current)
    return {"result": current}
# -------------------------------------------------------------------------


# reverse handler body ----------------------------------------------------
@app.post("/reverse")
async def reverser(req: Request):
    text = req.headers.get("string")
    if text == None:
        return JSONResponse(status_code=400, content="missing 'string' header")
    return {"result": text[::-1]}
# -------------------------------------------------------------------------


# list handler body -------------------------------------------------------
global_list = []

class RequestList(BaseModel):
    element: str = Field(min_length=1)

@app.put("/list")
async def list_handler(req: RequestList):
    global_list.append(req.element)
    list_size.set(len(global_list))
    return JSONResponse(status_code=200, content=f"{req.element} stored in elements list")

@app.get("/list")
def list_handler():
    return {"result": global_list}
# -------------------------------------------------------------------------


# calculator handler body -------------------------------------------------
class RequestCalculator(BaseModel):
    expr: str

@app.post("/calculator")
async def calculator(req: RequestCalculator):
    try:
        num1, operator, num2 = validateExpr(req.expr)
        last_calculator.set(result)
        result = doMath(num1, num2, operator)
    except CustomValidationError as err:
        return JSONResponse(
                status_code=err.status_code,
                content={"error": err.message}
            )
    if result % 1 == 0:
        return {"result": int(result)}
    return {"result": result}

def validateExpr(expr: str):
    try:
        num1, operator, num2 = expr.split(',')
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise CustomValidationError(status_code=400, message="invalid")
    
    return num1, operator, num2

def doMath(num1, num2, operator):
    result = 0
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise CustomValidationError(status_code=403, message="zerodiv")
        result = num1 / num2
    else:
        raise CustomValidationError(status_code=400, message="invalid")

    return result
# -------------------------------------------------------------------------
