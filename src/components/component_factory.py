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

        root_widget = self._create_widget(widget_tree, root)
        return root

    def _create_widget(self, widget, parent):
        self.logger.debug(f"Creating widget: {widget['type']} with attributes: {widget['attributes']}")
        tk_widget_class = self.widget_types.get(widget['type'])

        attributes = {k: v for k, v in widget['attributes'].items() if k != 'place'}

        tk_widget = tk_widget_class(parent, **attributes)

        if 'place' in widget['attributes']:
            tk_widget.place(**eval(widget['attributes']['place']))
        else:
            tk_widget.pack(expand=True)

        for child in widget['children']:
            child_widget = self._create_widget(child, tk_widget)

        return tk_widget