
## Run Locally

Clone the project

```bash
  https://github.com/cenizastevie/job_street_scrapy
```

Go to the project directory

```bash
  cd job_street_scrapy
```

Build docker image

```bash
  docker build -t job_street_scrapy . 
```

Run docker in production mode. 

```bash
  docker run -e DEFAULT_CMD="${PRODUCTION_CMD}" <image-name>
```

Run docker in debug mode. 

```bash
  docker run -e DEFAULT_CMD="${DEBUG_CMD}" <image-name>
```

Run docker unit tests. 

```bash
  docker run -e DEFAULT_CMD="${TEST_CMD}" <image-name>
```
