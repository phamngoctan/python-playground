Python docker start: navigate to the python-playground

```
docker build --target dev docker -t python
docker run -it -v ${PWD}:/work python sh
```