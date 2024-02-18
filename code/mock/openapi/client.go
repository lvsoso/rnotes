package openapisdk

import (
	"context"
	"errors"
	"fmt"
)

type Client struct {
	cli ClientAPI
}

func NewClient(cli ClientAPI) *Client {
	return &Client{cli: cli}
}

func (c *Client) GetUserSettings() error {

	userSettings, resp, err := c.cli.GetUserSettingsExecute(c.cli.GetUserSettings(context.Background()))
	if err != nil {
		println(resp.Status)
		println(resp.StatusCode)
		return err
	}
	if resp.StatusCode != 200 {
		return errors.New("erro status code")
	}
	for _, us := range userSettings {
		fmt.Printf("%+v", us)
	}
	return nil
}
