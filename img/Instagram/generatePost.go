package main

import (
	"log"
    "image"
    "os"
	"path/filepath"
    _ "image/jpeg"
    _ "image/png"
	"strconv"
	"time"
	
	"github.com/brunetto/goutils/debug"
)

func main() {
	defer debug.TimeMe(time.Now())
	var (
		outFile *os.File
		err error
		inFiles []string
		inFileName string
	)
	
	if outFile, err = os.Create("post.md"); err != nil {
		log.Fatal("Can't open post.md with error ", err)
	}
	defer outFile.Close()
	outFile.WriteString(`{{< gallery title="Example gallery" >}}`+"\n")
	
	
	if inFiles, err = filepath.Glob("*.jpg"); err != nil {
		log.Fatal("Error globbing files in this folder: ", err)
	}
	
	for _, inFileName = range inFiles {
		width, height := getImageDimension(inFileName)
		outFile.WriteString(`{{% galleryimage file="`+ inFileName +`" size="` + strconv.Itoa(width) + `x` + strconv.Itoa(height) + `" caption="" copyrightHolder=["BrunettoZiosi"](brunettoziosi.eu) %}}`+"\n")
	}

	outFile.WriteString(`{{< /gallery >}}`+"\n")
	outFile.WriteString(`{{% galleryinit %}}`+"\n")
}

// Taken from Sergio Tapia https://gist.github.com/sergiotapia/7882944
func getImageDimension(imagePath string) (int, int) {
    file, err := os.Open(imagePath)
	defer file.Close()
	
    if err != nil {
        log.Fatalf("Error opening image: %v\n", err)
    }
 
    image, _, err := image.DecodeConfig(file)
    if err != nil {
        log.Fatalf("Error decoding image %s: %v\n", imagePath, err)
    }
    return image.Width, image.Height
}

