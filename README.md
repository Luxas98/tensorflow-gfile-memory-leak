# Example of leaking Gfile from google cloud storage (GCS)


### Leak version
```bash
cd leak-version
docker build -f Dockerfile -t tf-gfile-leak .
docker run -ti tf-gfile-leak | tee mem-leak.log
```

We can see mem-leak.log or console, that memory gradually increases with each file

### NoLeak version
```bash
cd no-leak-version
docker build -f Dockerfile -t tf-gfile-leak .
docker run -ti tf-gfile-leak | tee mem-leak.log
```

mem-leak.log shows no problems, the only difference is the base in docker file 

python:3.7-stretch = leak
python:3.6-stretch = no-leak





