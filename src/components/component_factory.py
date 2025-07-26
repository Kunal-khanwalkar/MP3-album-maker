import tkinter as tk

class ComponentFactory:
    widget_types: dict[str, type] = {
        'root': tk.Tk,
        'Canvas': tk.Canvas,
        'Frame': tk.Frame,
        'Button': tk.Button
    }

    def __init__(self, logger):
        self.logger = logger

    def start(self, root: tk.Tk):
        root.mainloop()

    def component_generator(self, widget_tree):
        root = tk.Tk()
        root.title("MP3 Album Maker")

        # canvas = tk.Canvas(root, width=400, height=200)
        # canvas.pack()

        # frame = tk.Frame(canvas, bg="#80c1ff" bd="5")
        # frame.place(relx="0.5", rely= "0.1", relwidth= "0.75", relheight= "0.1", anchor= "n") # Layout position component
        # frame.pack()

        # button = tk.Button(canvas, bg="#80c1ff" bd="5")
        # button.place(relx="0.5", rely= "0.1", relwidth= "0.75", relheight= "0.1", anchor= "n") # Layout position component
        # button.pack()

        root_widget = self._create_widget(widget_tree, root)
        return root

    def _create_widget(self, widget, parent):
        self.logger.debug(f"Creating widget: {widget['type']} with attributes: {widget['attributes']}")
        tk_widget_class = self.widget_types.get(widget['type'])

        attributes = {k: v for k, v in widget['attributes'].items() if k != 'place'}

        # Attributes not working
        tk_widget = tk_widget_class(parent, **attributes)
        self.logger.debug("tk_widget generated, ", tk_widget, " with attributes: ", **attributes)

        if 'place' in widget['attributes']:
            tk_widget.place(**eval(widget['attributes']['place']))
            self.logger.debug("tk_widget, ", tk_widget)

        for child in widget['children']:
            child_widget = self._create_widget(child, tk_widget)
            child_widget.pack()

        tk_widget.pack()

        return tk_widget