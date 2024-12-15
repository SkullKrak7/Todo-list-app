import FreeSimpleGUI


Button = FreeSimpleGUI.Button("Convert")
feet = FreeSimpleGUI.Text("Enter Feet: ")
infeet = FreeSimpleGUI.InputText(key='infeet')
inch = FreeSimpleGUI.Text("Enter inches: ")
ininch = FreeSimpleGUI.InputText(key='ininch')
output = FreeSimpleGUI.Text("", key='output')
window = FreeSimpleGUI.Window("Convertor",[[feet ,infeet],[inch ,ininch],[Button, output ]])
while True:
    event, values = window.read()
    ft = float(values['infeet'])
    inn = float(values['ininch'])
    result = ft *0.3048 + inn * 0.0254
    window["output"].update(value = f"{result} m")
window.close()