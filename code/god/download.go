package god

import (
	"errors"
	"fmt"
	"io"
	"net/http"
	"os"
	"strconv"
	"sync"
)

type SliceStrings []string

func CreateHeader(k, v string) map[string]string {
	return map[string]string{k: v}
}

func log(v interface{}) {
	fmt.Printf("%+v\n", v)
}
func CreateHeaderS(k, v SliceStrings) map[string]string {
	res := map[string]string{}
	for idx, key := range k {
		res[key] = v[idx]
	}
	return res
}

func Download(
	url string,
	filename string,
	maxOpenfiles int,
	chunkSize int,
	parallelFailures int,
	maxRetries int,
	timeout int,
	allowRedirects bool,
	header map[string]string,
	callback func(n int),
) error {
	println("----------------------------")
	fmt.Printf("%+v\n", header)

	// header
	res, err := http.Head(url)
	if err != nil {
		return err
	}

	// get range
	if res.Header.Get("Accept-Ranges") != "bytes" {
		return errors.New("unsupport ranges")
	}
	log("supported ranges")

	// get length
	length, err := strconv.Atoi(res.Header.Get("Content-Length"))
	if err != nil {
		return errors.New("get length error")
	}
	log(length)

	start, end := 0, 0
	pool := make(chan int, maxOpenfiles)
	wg := &sync.WaitGroup{}

	for offset := 0; offset < length; offset += chunkSize + 1 {
		start = offset
		end = offset + chunkSize

		if offset > length {
			offset = length
		}

		log(fmt.Sprintf("%d-%d\n", start, end))
		// _ = pool
		// _ = wg
		buf := make([]byte, chunkSize)
		pool <- 1
		wg.Add(1)
		go download_chunk(pool, wg, buf, url, filename, start, end, callback)
	}

	wg.Wait()

	return nil
}

func download_chunk(pool chan int, wg *sync.WaitGroup, buf []byte, url string, filename string, start int, end int, callback func(n int)) (int, error) {
	defer func() {
		<-pool
		wg.Done()
	}()

	client := &http.Client{}
	req, err := http.NewRequest(http.MethodGet, url, nil)
	if err != nil {
		log(err)
		return 0, err
	}

	range_header := "bytes=" + strconv.Itoa(start) + "-" + strconv.Itoa(end)
	req.Header.Add("Range", range_header)
	resp, err := client.Do(req)
	if err != nil {
		log(err)
		return 0, err
	}
	defer resp.Body.Close()

	f, err := os.OpenFile(filename, os.O_WRONLY, os.ModeAppend)
	if err != nil {
		log(err)
		return 0, err
	}
	defer func() {
		f.Sync()
		f.Close()
	}()

	whence := io.SeekStart
	_, err = f.Seek(int64(start), whence)
	if err != nil {
		log(err)
		return 0, err
	}

	for {
		n, err := resp.Body.Read(buf)
		if err != nil && err != io.EOF {
			return 0, err
		}
		if n == 0 {
			break
		}
		if _, err := f.Write(buf[:n]); err != nil {
			return 0, err
		}
	}

	callback(end - start)

	return end - start, nil
}
