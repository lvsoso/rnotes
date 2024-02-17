package foo

import (
	"time"

	"github.com/jinzhu/gorm"
)

type User struct {
	gorm.Model
	Name string
	Age int
	Bithday time.Time
}


type Database interface {
    First(interface{})
}

func FooDatabaseCaseIndirectCall(db Database) int {
    var user User
    db.First(&user)
    return user.Age
}

func fooDatabaseCaseByValueFunc() int {
	return GetUserAgeValueFunc()
}

var GetUserAgeValueFunc = func() int {
	var user User
	db, err := gorm.Open("postgres", "host=myhost user=gorm dbname=gorm sslmode=disable password=mypassword")
    if err != nil {
        panic("connect fail")
    }
    res := db.First(&user)
    if res.Error != nil {
        panic("error")
    }
    db.Close()
    return user.Age
}

func fooBasic(num1 int, num2 int) int {
    return num1 + num2
}


func fooDatabaseCaseByFuncV2() int {
    return GetUserAgeFuncV2()
}

func GetUserAgeFuncV2() int {
    var user User
    db, err := gorm.Open("postgres", "host=myhost user=gorm dbname=gorm sslmode=disable password=mypassword")
    if err != nil {
        panic("connect fail")
    }
    res := db.First(&user)
    if res.Error != nil {
        panic("error")
    }
    db.Close()
    return user.Age
}