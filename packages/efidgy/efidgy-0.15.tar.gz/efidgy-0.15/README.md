# efidgy

Python bindings to efidgy services.


## Overview


### Environment

Environment in terms of efidgy package is a set of settings to work with efidgy backend.
Theese settings includes **customer code** and **access token** that will be used to communicate with backend.


### Unit System

If you will not set the unit system directly, efidgy will use current user settings: [console.efidgy.com/profile](https://console.efidgy.com/profile)

Anyway, it is a good practice to define the unit system in your code:

``` python
efidgy.env = efidgy.env.override(
    unit_system=efidgy.models.UnitSystem.IMPERIAL,
)
```


### Credentials

efidgy.env is initialized with settings fetched from the shell environment. The following environment variables are used:

 * EFIDGY_ACCESS_TOKEN -- You can get one at [console.efidgy.com/profile/company](https://console.efidgy.com/profile/company)
 * EFIDGY_CUSTOMER_CODE -- See [console.efidgy.com/profile/tokens](https://console.efidgy.com/profile/tokens)

You can always override code and/or token with the code like this:

``` python
efidgy.env = efidgy.env.override(
    code='hardcoded customer code',
)
```


## API documentation

Find out more at: [efidgy.com/docs](https://efidgy.com/docs)


## Sample usage

``` sh
export EFIDGY_CUSTOMER_CODE=code  # https://console.efidgy.com/profile/company
export EFIDGY_ACCESS_TOKEN=token  # https://console.efidgy.com/profile/tokens
```


### Sync API

``` python
import datetime
import efidgy


def create_project():
    project = efidgy.models.Project.service.create(
        name='Demo',
        currency='USD',
        project_type=efidgy.models.ProjectTypeCode.IDD_OR,
        shared_mode=efidgy.models.SharedMode.PRIVATE,
    )

    store_address = '6133 Broadway Terr., Oakland, CA 94618, USA'
    lat, lon = efidgy.tools.geocode(store_address)
    store = efidgy.models.idd_or.Store.service.create(
        project=project,
        address=store_address,
        lat=lat,
        lon=lon,
        name='Delivery Inc.',
        open_time=datetime.time(8, 0),
        close_time=datetime.time(18, 0),
    )

    efidgy.models.idd_or.Vehicle.service.create(
        project=project,
        store=store,
        name='Gary Bailey',
        fuel_consumption=11.76,
        fuel_price=3.25,
        salary_per_duration=21,
        duration_limit=datetime.timedelta(hours=9),
    )

    order_address = '1 Downey Pl, Oakland, CA 94610, USA'
    lat, lon = efidgy.tools.geocode(order_address)
    efidgy.models.idd_or.Order.service.create(
        project=project,
        store=store,
        name='#00001',
        address=order_address,
        lat=lat,
        lon=lon,
        ready_time=datetime.time(8, 0),
        delivery_time_from=datetime.time(12, 0),
        delivery_time_to=datetime.time(16, 0),
        load_duration=datetime.timedelta(minutes=1),
        unload_duration=datetime.timedelta(minutes=5),
        items=1,
        volume=3.53,
        weight=22.05,
    )

    return project


def solve(project):
    project.computate()

    solutions = efidgy.models.Solution.service.all(
        project=project,
    )

    if not solutions:
        return None

    return solutions[0]


def report(project, solution):
    print('Total Cost: {cost:.2f}{currency}'.format(
        cost=solution.cost,
        currency=project.currency.symbol,
    ))

    vehicles = efidgy.models.idd_or.Vehicle.service.all(
        project=project,
        solution=solution,
    )

    for vehicle in vehicles:
        print('{vehicle} Schedule'.format(
            vehicle=vehicle.name,
        ))
        if vehicle.route is not None:
            arr = vehicle.route.start_time
            for schedule in vehicle.route.schedule:
                dep = schedule.departure_time
                print('{at}\t{arr}\t{dep}'.format(
                    at=schedule.start_point.name,
                    arr=arr,
                    dep=dep,
                ))
                arr = schedule.arrival_time
            if vehicle.route.schedule:
                print('{at}\t{arr}\t{dep}'.format(
                    at=vehicle.route.schedule[-1].end_point.name,
                    arr=vehicle.route.schedule[-1].arrival_time,
                    dep='',
                ))


def main():
    project = create_project()
    solution = solve(project)
    if solution:
        report(project, solution)


if __name__ == '__main__':
    main()
```


### Output
```
Total Cost: 12.51$
Gary Bailey Schedule
Delivery Inc.   15:45:00        15:46:00
#00001          15:55:00        16:00:00
Delivery Inc.   16:09:00
```


### Async API

``` python
import datetime
import asyncio
import efidgy.asyncapi as efidgy


async def create_project():
    project = await efidgy.models.Project.service.create(
        name='Demo',
        currency='USD',
        project_type=efidgy.models.ProjectTypeCode.IDD_OR,
        shared_mode=efidgy.models.SharedMode.PRIVATE,
    )

    store_address = '6133 Broadway Terr., Oakland, CA 94618, USA'
    lat, lon = await efidgy.tools.geocode(store_address)
    store = await efidgy.models.idd_or.Store.service.create(
        project=project,
        address=store_address,
        lat=lat,
        lon=lon,
        name='Delivery Inc.',
        open_time=datetime.time(8, 0),
        close_time=datetime.time(18, 0),
    )

    await efidgy.models.idd_or.Vehicle.service.create(
        project=project,
        store=store,
        name='Gary Bailey',
        fuel_consumption=11.76,
        fuel_price=3.25,
        salary_per_duration=21,
        duration_limit=datetime.timedelta(hours=9),
    )

    order_address = '1 Downey Pl, Oakland, CA 94610, USA'
    lat, lon = await efidgy.tools.geocode(order_address)
    await efidgy.models.idd_or.Order.service.create(
        project=project,
        store=store,
        name='#00001',
        address=order_address,
        lat=lat,
        lon=lon,
        ready_time=datetime.time(8, 0),
        delivery_time_from=datetime.time(12, 0),
        delivery_time_to=datetime.time(16, 0),
        load_duration=datetime.timedelta(minutes=1),
        unload_duration=datetime.timedelta(minutes=5),
        items=1,
        volume=3.53,
        weight=22.05,
    )

    return project


async def solve(project):
    await project.computate()

    solutions = await efidgy.models.Solution.service.all(
        project=project,
    )

    if not solutions:
        return None

    return solutions[0]


async def report(project, solution):
    print('Total Cost: {cost:.2f}{currency}'.format(
        cost=solution.cost,
        currency=project.currency.symbol,
    ))

    vehicles = await efidgy.models.idd_or.Vehicle.service.all(
        project=project,
        solution=solution,
    )

    for vehicle in vehicles:
        print('{vehicle} Schedule'.format(
            vehicle=vehicle.name,
        ))
        if vehicle.route is not None:
            arr = vehicle.route.start_time
            for schedule in vehicle.route.schedule:
                dep = schedule.departure_time
                print('{at}\t{arr}\t{dep}'.format(
                    at=schedule.start_point.name,
                    arr=arr,
                    dep=dep,
                ))
                arr = schedule.arrival_time
            if vehicle.route.schedule:
                print('{at}\t{arr}\t{dep}'.format(
                    at=vehicle.route.schedule[-1].end_point.name,
                    arr=vehicle.route.schedule[-1].arrival_time,
                    dep='',
                ))


async def main():
    project = await create_project()
    solution = await solve(project)
    if solution:
        await report(project, solution)


if __name__ == '__main__':
    asyncio.run(main())
```


### Output
```
Total Cost: 12.51$
Gary Bailey Schedule
Delivery Inc.   15:45:00        15:46:00
#00001          15:55:00        16:00:00
Delivery Inc.   16:09:00
```

