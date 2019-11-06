module FSM(reset, clock, Din, Dout);
  input reset;
  input clock;
  input Din;
  output Dout;

  reg Dout;

  parameter [1:0] S0 = 0, S1 = 1, S2 = 2;
  reg [1:0] current_state, next_state;

  always @(posedge clock or posedge reset)
  begin: SYNCH
    if (reset == 1'b1)
       current_state <= S0;
    else
       current_state <= next_state;
  end

  always @(current_state or Din)
  begin: COMBIN
     case (current_state)
        S0:
        begin
          if (Din == 1'b1)
             begin
             next_state <= S1;
             end
          else if (Din == 1'b0)
             begin
             next_state <= S0;
             end
          Dout <= 1'b0;

        end

        S1:
        begin
          if (Din == 1'b0)
             begin
             next_state <= S2;
             end
          else if (Din == 1'b1)
             begin
             next_state <= S1;
             end
          Dout <= 1'b0;

        end

        S2:
        begin
          if (Din == 1'b1)
             begin
             next_state <= S1;
             end
          else if (Din == 1'b0)
             begin
             next_state <= S0;
             end
          Dout <= 1'b1;

        end


        default:
          next_state <= S0;
     endcase
  end

endmodule
