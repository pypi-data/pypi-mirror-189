wyp
===

Simple text-based webapp for plotting timeseries from wandb.
The philosophy behind WYWIWYP (What You Write Is What You Plot) or in short WYP (Write Your Plot) is to define the plots with a simple text-based interface.


### Get Started

Install the package

```
pip install wyp
```

Check that you are logged in wandb and lunch the webapp:

```
wandb login
wyp
```

You can connect to [http://localhost:5000/](http://localhost:5000/).

### Development

Clone this repository and run `python wyp/serve.py`.

To work on the frontend:

```bash
npm install
npm run dev
```

### Deploy

Check the `Makefile` to make the python package and upload it. 
We build the svelte app and copy the static files served to the clients (HTML, JS, ...) into the python package. 


### TODO

- [ ] Improve autocompletion for available plot keys
- [ ] Improve autocompletion for available metrics in the wandb runs
- [ ] Add CI for building the pip package at every release
- [ ] Add `columns`, `rows`, `hue`, `linestyle` to make facet plots
- [ ] Support multiple metrics `y` in a plot
- [ ] Add a table with the runs and the config keys
- [ ] Export to PNG
- [ ] Export to HTML with the data inlined (read only)
- [ ] Save exported HTML to gs:// for sharing quickly