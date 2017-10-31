all: send

clean:
	rm main

run: main
	./main

main: main.cc
	g++ -o main main.cc

send: main.cc
	netoi-check -s main.cc -p eclipse
