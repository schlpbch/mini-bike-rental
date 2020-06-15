import uvicorn
from fastapi import FastAPI

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List

from model import BikeState, BikeType, Bike, Station


# Data for our small world.

bike1 = Bike(
    id="B1", type=BikeType.NORMAL, stationed_at="S1", state=BikeState.FREE, battery=49
)
bike2 = Bike(
    id="B2", type=BikeType.FAST, stationed_at="S2", state=BikeState.FREE, battery=100
)
bike3 = Bike(
    id="B3", type=BikeType.NORMAL, stationed_at="S1", state=BikeState.BROKEN, battery=0
)

bikes = {}
bikes[bike1.id] = bike1
bikes[bike2.id] = bike2
bikes[bike3.id] = bike3

station1 = Station(id="S1", name="Bern, Bahnhof", bikes=["B1", "B3"])
station2 = Station(id="S2", name="Bern, Wyleregg", bikes=["B2"])
station3 = Station(id="S3", name="Bern, Wankdorf", bikes=[])

stations = {}
stations[station1.id] = station1
stations[station2.id] = station2
stations[station3.id] = station3


# The API

app = FastAPI(
    description="A small API for a small bike rental based in Bern.",
    title="Mini Bike Rental",
)


@app.get("/", tags=["version"])
def get_version():
    return {"Mini Bike Rental": "v. 0.1.0"}


## Stations


@app.get("/stations/", response_model=List[Station], tags=["stations"])
def read_stations():
    return list(stations.values())


@app.get("/stations/{station_id}", response_model=Station, tags=["stations"])
def read_station(station_id: str):
    if station_id in stations:
        return stations[station_id]
    else:
        return JSONResponse(
            status_code=404, content=f"stationId '{station_id}' not found"
        )


## Bikes


@app.get("/bikes/", response_model=List[Bike], tags=["bikes"])
def read_bikes():
    return list(bikes.values())


@app.get("/bikes/{bike_id}", response_model=Bike, tags=["bikes"])
def read_bike(bike_id: str):
    if bike_id in bikes:
        return bikes[bike_id]
    else:
        return JSONResponse(status_code=404, content=f"bikeId '{bike_id}' not found")


@app.post("/bikes/{bike_id}", response_model=Bike, tags=["bikes"])
def add_bike(bike_id: str, bike: Bike):
    if not bike_id in bikes:
        bikes[bike_id] = bike
        return bike
    else:
        return JSONResponse(
            status_code=404, content=f"bikeId '{bike_id}' already exists"
        )


@app.put("/bikes/{bike_id}", response_model=Bike, tags=["bikes"])
def update_bike(bike_id: str, bike: Bike):
    if bike_id in bikes:
        bikes[bike_id] = bike
        return bike
    else:
        return JSONResponse(status_code=404, content=f"bikeId '{bike_id}' not found")


@app.patch("/bikes/{bike_id}", response_model=Bike, tags=["bikes"])
def partial_update_bike(bike_id: str, bike: Bike):
    if bike_id in bikes:
        updated_bike = bikes[bike_id]
        if bike.stationed_at is not None:
            updated_bike.stationed_at = bike.stationed_at
        if bike.state is not None:
            updated_bike.state = bike.state
        if bike.battery is not None:
            updated_bike.battery = bike.battery
        bikes[bike_id] = updated_bike
        return updated_bike
    else:
        return JSONResponse(status_code=404, content=f"bikeId '{bike_id}' not found")


@app.delete("/bikes/{bike_id}", tags=["bikes"])
def delete_bike(bike_id: str):
    if bike_id in bikes:
        station_id = bikes[bike_id].stationed_at
        stations[station_id].bikes.remove(bike_id)
        del bikes[bike_id]
        return JSONResponse(
            status_code=200, content=f"bike with id '{bike_id}' deleted"
        )
    else:
        return JSONResponse(status_code=404, content=f"bikeId '{bike_id}' not found")


# Start server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
