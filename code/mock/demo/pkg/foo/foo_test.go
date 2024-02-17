package foo_test

import (
	. "demo/pkg/foo"
	"testing"

	"bou.ke/monkey"
	"github.com/golang/mock/gomock"
	"github.com/prashantv/gostub"
	"github.com/stretchr/testify/assert"
)

func TestFooBasic(t *testing.T) {
    expect := 2
    actual := FooBasic(1, 1)
    assert.Equal(t, expect, actual)
}


func TestFooDatabaseByValueFunc(t *testing.T) {
    want := 1
    stub := gostub.Stub(&GetUserAgeValueFunc, func() int {
        return 1
    })
    defer stub.Reset()
    actual := FooDatabaseCaseByValueFunc()
    assert.Equal(t, want, actual)
}

func TestFooDatabaseByFunc_monkey(t *testing.T){
	want := 1
	patch := monkey.Patch(GetUserAgeFuncV2, func() int {
		return 1
	})

	defer patch.Restore()
	actual := FooDatabaseCaseByFuncV2()
	assert.Equal(t, want, actual)
}


func TestFooDatabaseGomock(t *testing.T){
	want := 1
	var user User
	ctrl := gomock.NewController(t)
	defer ctrl.Finish()
	m := NewMockDatabase(ctrl)
	m.EXPECT().First(gomock.Eq(&user)).SetArg(0, User{Age:1})
	actual := FooDatabaseCaseIndirectCall(m)
    assert.Equal(t, want, actual)
}