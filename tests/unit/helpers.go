package data_parser

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
)

func ReadFile(filePath string) ([]byte, error) {
	data, err := ioutil.ReadFile(filePath)
	if err != nil {
		return nil, err
	}
	return data, nil
}

func WriteFile(filePath string, data []byte) error {
	dir := filepath.Dir(filePath)
	if _, err := os.Stat(dir); os.IsNotExist(err) {
		err = os.MkdirAll(dir, os.ModePerm)
		if err != nil {
			return err
		}
	}
	f, err := os.Create(filePath)
	if err != nil {
		return err
	}
	defer f.Close()
	_, err = f.Write(data)
	return err
}

func JSONMarshal(data interface{}) (string, error) {
	jsonData, err := json.MarshalIndent(data, "", "\t")
	if err != nil {
		return "", err
	}
	return string(jsonData), nil
}

func JSONUnmarshal(data []byte, target interface{}) error {
	return json.Unmarshal(data, target)
}

func LogError(message string) {
	log.Println("ERROR:", message)
}

func LogWarning(message string) {
	log.Println("WARNING:", message)
}