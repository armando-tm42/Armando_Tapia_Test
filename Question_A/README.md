# Overlap lines test script
This program deals with identifying if two lines overlap or not

## hypothesis
An interval is defined as a connected portion of a real line, in this case the x-axis is the real line and the line (x_1,x_2) could be interpreted as an interval. So, if we need to know if the lines (x_1,x_2) and (x_3,x_4) overlaps, we just create two intervals using these set of points and find the intercept between the intervals that also represent the overlap between the lines.

## Usage
First provide the set of test points in the order (x_1,x_2) , (x_3,x_4).
```python
>>> Enter x values (x_1,x_2,x_3,x4): 1 5 6 8
```
Using the interval library, two interval objects are created simulating the lines. The starting points of the lines are (x_1,x_3) and the endpoints (x_2,x_4).
```python ​
line_a = interval[x_1,x_2]
line_b = interval[x_3,x_4]
```
Intercepting both lines (intervals) we can  know if they overlap or not.

```python ​
overlap_points = line_a&line_b  
```
Now using pyplot, with the object hline we create the x axis line and using vline object create the xticks
```python
def plot_line(ax,x_a,
              x_b,y,
             color):
    ax.hlines(y,x_a,x_b,color=color)
    ax.vlines(x_a, y - 0.01 / 2., y + 0.01 / 2.,colors=color)
    ax.vlines(x_b, y - 0.01 / 2., y + 0.01 / 2.,colors=color)
    ax.text(x_a, y+0.01,x_a,horizontalalignment='center')
    ax.text(x_b, y+0.01,x_b,horizontalalignment='center')        
```
 Finally we plot the lines and if the intersection object is not empty the lines overlaps else they don't.
```python
if len(overlap_points) != 0:
    plot_line(ax,overlap_points[0][0],overlap_points[0][1],color='red',y=0)
    ax.text(xmax/2,0.03,'The two lines overlap',horizontalalignment='center')
else:
    ax.text(xmax/2,0.03,'The two lines no overlap',horizontalalignment='center')
```
Output

## License
to define
