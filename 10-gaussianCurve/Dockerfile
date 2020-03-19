FROM golang:latest

LABEL maintainer="Mathis Van Eetvelde"

WORKDIR /app

COPY . .

RUN go get -d github.com/gorilla/mux

EXPOSE 8080

RUN go build -o main .

CMD ["./main"] 
