<h1>SNAP (Stanford Network Analysis Platform)</h1>
<p>Stanford Network Analysis Platform (SNAP) is a general purpose, high
performance system for analysis and manipulation of large networks.
SNAP is written in C++ and it scales to massive graphs with hundreds
of millions of nodes and billions of edges.</p>

## INSTALLATION
1. ```bash
   pip install -r requirements.txt
   ```
2. That's it
<br>
<h2>USING THE PACKAGE</h2>
<p>After installing all dependencies, you're able to follow this formula in the command line</p>
<h3> Command Line Formula</h3>

```bash
python .\<2d or 3d>.py -a .\testCases\<test file name>.txt
```
Example
```bash
python .\2d.py -a .\testCases\10x10.txt
```
<h3>OUTPUTS</h3>

* Runtimes for each algorithm (graph creation, filtering, and BFS)
* Directory of where the visualization of the graph is
