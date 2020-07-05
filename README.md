# covid-plotter

Simple python webapp to plot graphs on current Covid-19 situation around the world

## Before you start

You need to define the method for delivering static assets, in this case, images. This is done
in `config.py`. Just modify the following line.

```python3
STATIC_CONT = 'https://www.example.com/plots/'
```

I personally have a separate volume under my nginx container, which is shared with this app.
Once stats of a country are requested the resulting graph is stored into that volume and served
by the nginx. I have configured that url in my version of `config.py`.

## Testing

First of all jump to the webapp directory. It's probably wise to check that
nothing has got broken. Rename `test-fetchPatientData-Dockerfile` to `Dockerfile`
build and run. This does very basic unit testing.

```bash
cp Dockerfile true-Dockerfile
cp test-fetchPatientData-Dockerfile Dockerfile
docker build --tag test-web:01 .
docker run --rm -it  test-web:01

```

You should see something like this:

```bash
Success
OK: The lengths in total cases and daily new cases match
Site < http://asdfasdfasdf.ex.gov/ > unavailable...
all tests PASSED
-----------------------
```

## Running

Build and run.
```bash
cd webapp
docker build --tag covid-tracker:01 .
docker run -it covid-tracker:01
```
