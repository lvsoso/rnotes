package god

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func callback(n int) {
	fmt.Println(n)
}

func TestXxx(t *testing.T) {
	url := "https://github.com/chenzomi12/DeepLearningSystem/releases/download/AISystem/02Hardware_slide.zip"
	filename := "/home/lv/lvsoso/rnotes/code/god/testfile"
	maxOpenfiles := 10
	chunkSize := 10 * 1024 * 1024
	parallelFailures := 3
	maxRetries := 3
	timeout := 5000
	allowRedirects := true
	headers := map[string]string{}
	callback := callback

	err := Download(
		url,
		filename,
		maxOpenfiles,
		chunkSize,
		parallelFailures,
		maxRetries,
		timeout, allowRedirects, headers, callback)
	assert.Nil(t, err)

}
