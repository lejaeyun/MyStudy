module FlipFlopCE_tb;

reg CLK;
reg Ce;
reg Din;
wire Qout;
reg RST;

FlipFlopCE
 U0 (
  .CLK(CLK),
  .Ce(Ce),
  .Din(Din),
  .Qout(Qout),
  .RST(RST));
  initial
  begin
    CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b0;
    #100 CLK = 1'b1;
    #100 CLK = 1'b0;
  end

  initial
  begin
    RST = 1'b1;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b1;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
    #100 RST = 1'b0;
  end

  initial
  begin
    Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b1;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
    #100 Din = 1'b0;
  end

  initial
  begin
    CE = 1'b0;
    #100 CE = 1'b0;
    #100 CE = 1'b0;
    #100 CE = 1'b0;
    #100 CE = 1'b0;
    #100 CE = 1'b1;
    #100 CE = 1'b0;
    #100 CE = 1'b1;
    #100 CE = 1'b0;
    #100 CE = 1'b0;
    #100 CE = 1'b0;
    #100 CE = 1'b1;
    #100 CE = 1'b0;
    #100 CE = 1'b1;
    #100 CE = 1'b0;
    #100 CE = 1'b0;
    #100 CE = 1'b0;
    #100 CE = 1'b1;
    #100 CE = 1'b0;
    #100 CE = 1'b1;
    #100 CE = 1'b0;
    #100 CE = 1'b0;
    #100 CE = 1'b0;
    #100 CE = 1'b1;
    #100 CE = 1'b0;
    #100 CE = 1'b1;
    #100 CE = 1'b0;
    #100 CE = 1'b1;
    #100 CE = 1'b0;
    #100 CE = 1'b0;
    #100 CE = 1'b0;
    #100 CE = 1'b0;
    #100 CE = 1'b0;
    #100 CE = 1'b0;
    #100 CE = 1'b0;
    #100 CE = 1'b0;
    #100 CE = 1'b0;
    #100 CE = 1'b0;
    #100 CE = 1'b0;
    #100 CE = 1'b1;
    #100 CE = 1'b0;
  end



endmodule
