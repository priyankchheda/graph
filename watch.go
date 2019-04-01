package main

import (
	"os/exec"
	"time"

	"github.com/rivo/tview"
)

func main() {
	app := tview.NewApplication()
	textView := tview.NewTextView().SetChangedFunc(func() {
		app.Draw()
	})

	go func() {
		for {
			cmd := exec.Command("tree")
			output, err := cmd.Output()
			if err != nil {
				panic(err)
			}

			textView.Clear()

			prefix := "Every 2s : tree\n" + time.Now().Format("2006-01-02 15:04:05") + "\n\n"
			textView.SetText(prefix + string(output))
			time.Sleep(2 * time.Second)
		}
	}()

	if err := app.SetRoot(textView, true).Run(); err != nil {
		panic(err)
	}
}
