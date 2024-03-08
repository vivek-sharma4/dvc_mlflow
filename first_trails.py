import mlflow


def calculate(x,y):
    return (x-y)


if __name__=='__main__':
    x,y=100,200
    
    with mlflow.start_run():
        result=calculate(x,y)
    
        print(f"my result is {result}")