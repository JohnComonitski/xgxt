# Simple xG xT Generation

Generate xG and xT values to improve your football match analysis using a static xG and xT model.


## Getting Started
1. Clone the repository

   ```shell
   git clone https://github.com/JohnComonitski/xgxt.git
   ```

2. Copy the files `utils.py`, `xg.py` and `xt.py` into your project

3. Install the Numpy dependencies

   ```shell
   pip install numpy
   ```

 4. Import the libraries into your project

     ```python
     from xg import *
     from xt import *
     ```

  5. Use the `get_xg` and `get_xt` functions to generate xG and xT values

     ```python
     coords = (100, 50)
     print(get_xg(coords))
     print(get_xt(coords))
     ```
 
