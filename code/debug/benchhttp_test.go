package benchhttp

import (
	"bytes"
	"io"
	"io/ioutil"
	"net/http"
	"net/http/httptest"
	"testing"
)

func Benchmark(b *testing.B) {
	data := []byte("Foobar")
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, req *http.Request) {
		w.Write(data)
	}))
	defer srv.Close()

	payload := []byte(`{"key":"value"}`)

	http.DefaultTransport.(*http.Transport).MaxConnsPerHost = 0
	b.RunParallel(func(pb *testing.PB) {
		for pb.Next() {
			// resp, err := http.Get(srv.URL)
			resp, err := http.Post(srv.URL, "application/json", bytes.NewBuffer(payload))
			if err != nil {
				panic(err)
			}

			if err != nil {
				b.Fatal(err)
			}
			io.Copy(ioutil.Discard, resp.Body)
			resp.Body.Close()
		}
	})
}
