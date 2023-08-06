# MuPhyN - Multi Physical Nexus

MatLab/Simulink is a very powerful tool that allows engineers to simulate complex multi-physical systems. Free and open-source tools exist such as Scilab + Xcos or Octave that tries to be compatible with MatLab/Simulink, but the approach of MuPhyN is to replicate the power and ease of use of the MatLab/Simulink combination by using (i)Python instead of MatLab combined with the MuPhyN graphical interface instead of Simulink.

Free libraries such as scipy and numpy offer numerical tools that can replicate most of MatLab toolboxes, and implementing them into new boxes in MuPhyN is trivial thanks to easily expandables libraries of boxes.

MuPhyn is capable of running into an iPython interactive shell while having access to the namespace of the shell. This means that python code can be run in the shell to dynamically generate modelisation parameters that can be directly used into the MuPhyN model of the simulated system.

MuPhyN is also intendend to be expandable to other simulation tools. A connection to OpenModelica is being developed to simulate different kinds of systems with lumped elements. Connection to open source finite element analysis softwares such as FEATools or field solver tools like openEMS or FEMM are also considered.

it is based on a Qt interface and uses a simulator core. It is fully written in Python and uses YAML as the descriptive language. The library feature proposed allows users to add as many boxes and schedulers as they want.

## Install

Install using pip:
```bash
pip install muphyn
```

## Running in standalone mode

Launch the software:
```bash
python3 -m muphyn
```

## Running in an iPython interactive shell

Start iPython:
```bash
iPython3
```

Then load the MuPhyN extension, and run the MuPhyN magic command
```bash
%load_ext muphyn
%muphyn
```

## Usage

### Drag drop

You can easily drag / drop elements from the library.
Once dropped, you can link the inputs and the outputs of the box.
You can also edit the properties of the boxes in order to change their behaviours.
Once everything is setted up, you only need to press the F5 key or click on the "Simulation > Lancer" menu.

![](https://media3.giphy.com/media/SaTScRBbeSNChgjagW/giphy.gif)

### Select library


Use the "Affichage > Bibliothèques" sub menus to add the libraries
Default libraries are located as it : 
- [MuPhyN_Folder]/box_library
- [MuPhyN_Folder]/scheduler_library
- [MuPhyN_Folder]/user_box

![](https://media4.giphy.com/media/uPfHccujlpxyGAkyF4/giphy.gif)

## Developpement

### Current Current Features 

- Fixed-step simulation 
- Basic boxes : Addition, Amplifier, Constant, Derivator, Graph, Integrator, Multiplier, Ramp, Sine, Square, Step
- Fixed-step simulation 
- Basic boxes : Addition, Amplifier, Constant, Derivator, Graph, Integrator, Multiplier, Ramp, Sine, Square, Step
- Schedulers : Default
- Transfer Function box using scipy ODE solver
- Libraries management for both the boxes and the schedulers
- Draggable and droppable element from the library
- Properties panel for the dragged boxes
- Draggable links between the inputs and outputs of boxes
- Basic user interface: 
  - File drag / drop in the interface.
  - Show recent files
  - Undo / Redo
  - Copy / Cut / Paste
- Transfer Function box using scipy ODE solver
- Libraries management for both the boxes and the schedulers
- Draggable and droppable element from the library
- Properties panel for the dragged boxes
- Draggable links between the inputs and outputs of boxes
- Basic user interface: 
  - File drag / drop in the interface.
  - Show recent files
  - Undo / Redo
  - Copy / Cut / Paste

### Todo 

- Allow to edit the prompted text on the boxes.
- Add the box composite diagram editor.
- Allow to save composite boxes.
- Allow to open composite boxes.
- Allow to compile composite boxes.
- Show better visual feedback for the link creation.
- Add a progress bar for the simulation part.
- Add a logs manager to retrace what happen when an error occur.
- Add some popups to describes the errors currently rendered in the prompt.
- Add some popups menu when right click on elements.
- Add a library popup when drag / drop a link to show compatible box.
- Allows the user to pick from the library popup a compatible box, which will be added already connected to the diagram.
- Add some popups to tell the user when an action is correctly done.
- Add a dialog to edit the parameters of the software.
- Add a dialog to show an help to use the software.
- Add a dialog to show the informations about the softawre.
- Add theme manager.
- Finish the formula box
- Finish the reccurence box
- Add a vectorial / matrix simulation mode
- Add a mux box
- Add a demux box
- Allow to pause / restart / stop a heavy simulation.
- Add a debug mode to see what happens on the different link by adding a step by step simulation.
- Add openned matplotlib chart in the dialog manager.
- Add a wizard fot the schedulers creation.
- Add a code editor for the schedulers and the coded boxes.
- Add a language dialog to manage / create the software language.
- Allow to change the displayed language.
- Add a theme dialog to manage / create the software themes.
- Allow to change the displayed theme.
- Add a signal analysis library.

### Known bugs

- When a text from an IO of a box is edited, it is not edited in the diagram.
- Some lags with the links rendering exists.
