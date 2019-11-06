module FlipFlop(Din,CLK,RST,Qout);

input Din;
input CLK;
input RST;
output Qout;

wire  w0;
wire  w1;
wire  w2;
wire  w3;

assign w3 = Din;
assign w2 = CLK;
assign w1 = RST;
assign Qout = w0;

PNU_DFF
     s0 (
      .Q(w0),
      .reset(w1),
      .clock(w2),
      .D(w3));

endmodule

