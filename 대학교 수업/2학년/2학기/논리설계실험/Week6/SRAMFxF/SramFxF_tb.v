module SramFxF_tb;

reg [1:0] ADRESS;
wire [3:0] DataOut;
reg [3:0] Din;
reg RST;
reg RW;

SramFxF
 U0 (
  .ADRESS(ADRESS),
  .DataOut(DataOut),
  .Din(Din),
  .RST(RST),
  .RW(RW));

  initial
  begin
    ADRESS = 2'b00;
    #900 ADRESS = 2'b10;
    #100 ADRESS = 2'b00;
    #200 ADRESS = 2'b01;
    #100 ADRESS = 2'b00;
    #200 ADRESS = 2'b11;
    #100 ADRESS = 2'b00;
  end

  initial
  begin
    Din = 4'b0000;
    #600 Din = 4'b0001;
    #100 Din = 4'b0000;
    #200 Din = 4'b0010;
    #100 Din = 4'b0000;
    #200 Din = 4'b0100;
    #100 Din = 4'b0000;
    #200 Din = 4'b1000;
    #100 Din = 4'b0000;
  end

  initial
  begin
    RST = 1'b1;
    #100 RST = 1'b0;
  end

  initial
  begin
    RW = 1'b0;
    #500 RW = 1'b1;
    #200 RW = 1'b0;
    #100 RW = 1'b1;
    #200 RW = 1'b0;
    #100 RW = 1'b1;
    #200 RW = 1'b0;
    #100 RW = 1'b1;
    #200 RW = 1'b0;
  end

endmodule
