from manimlib.imports import *

class GradientDescent(Scene):

    def construct(self):
      quote = TextMobject("Imagine we want to find the minimum of a function")
      quote.set_color(RED)
      quote.to_edge(UP)
      quote2 = TextMobject("The function might look something as follows")
      quote2.set_color(YELLOW)

      eq1=TextMobject("$x^4 - x^3-6x^2+4x+12$")
      eq1.shift(2*UP)  # shifting units up or down

      self.add(quote)
      self.wait(4)
      self.play(Transform(quote,quote2))
      self.wait(2)
      self.play(FadeOut(quote))
      self.play(Write(eq1))
      self.wait(4)

class PlotGB(GraphScene):
    CONFIG = {
        "x_min" : -1.8,
        "x_max" : 3.1,
        "y_min" : 0,
        "y_max" : 32,
        "graph_origin" : 2.5 * DOWN,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-1,3,1),
        "y_labeled_nums" :range(0,30,5),
    }   
    def construct(self):
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        vert_line = self.get_vertical_line_to_graph(TAU,func_graph,color=YELLOW)
        graph_lab = self.get_graph_label(func_graph, label = "Our function")

        self.play(ShowCreation(func_graph))
        self.wait(3)

    def func_to_graph(self,x):
        return x ** 4 - x ** 3 - 6 * x ** 2 + 4*x + 12

