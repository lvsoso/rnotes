package openapisdk

import (
	"context"
	"net/http"
	mock "openapisdk/mock"
	"testing"

	openapi "github.com/GIT_USER_ID/GIT_REPO_ID"

	"github.com/golang/mock/gomock"
)

func TestUserAPI(t *testing.T) {
	ctl := gomock.NewController(t)
	defer ctl.Finish()

	mockClient := mock.NewMockClientAPI(ctl)
	client := NewClient(mockClient)

	gomock.InOrder(
		mockClient.EXPECT().GetUserSettings(context.Background()),
		mockClient.EXPECT().GetUserSettingsExecute(gomock.Any()).Return(
			[]openapi.UserSettings{},
			&http.Response{StatusCode: 200},
			nil),
	)
	err := client.GetUserSettings()
	if err != nil {
		t.Fatal(err)
	}
	t.Log(client)
}
