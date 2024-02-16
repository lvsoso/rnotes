package roll

import (
        "testing"
)

func TestGenerateNumber(t *testing.T) {
        result := generateNumber()

        if result == "" {
                t.Error("got an empty string")
        }
}
