module FSM_tb;

parameter S0 = 0;
parameter S1 = 1;
parameter S2 = 2;

reg Din;
wire Dout;
reg clock;
reg reset;

FSM
 #(
  .S0(0),
  .S1(1),
  .S2(2))
 U0 (
  .Din(Din),
  .Dout(Dout),
  .clock(clock),
  .reset(reset));

  initial
  begin
    Din = 1'b0;
    #800 Din = 1'b1;
    #200 Din = 1'b0;
    #200 Din = 1'b1;
    #200 Din = 1'b0;
    #400 Din = 1'b1;
    #400 Din = 1'b0;
    #200 Din = 1'b1;
    #600 Din = 1'b0;
    #700 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
  end

  initial
  begin
    clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
    #100 clock = 1'b1;
    #100 clock = 1'b0;
  end

  initial
  begin
    reset = 1'b0;
    #200 reset = 1'b1;
    #200 reset = 1'b0;
  end

endmodule
