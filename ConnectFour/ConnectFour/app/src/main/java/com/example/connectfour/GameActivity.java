package com.example.connectfour;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.view.View;
import android.widget.Button;
import androidx.gridlayout.widget.GridLayout;

import android.widget.ImageView;
import android.widget.TextView;

import java.util.ArrayList;

public class GameActivity extends AppCompatActivity {

    boolean p1Turn = true;
    public ArrayList<ArrayList<String>> gameArray = new ArrayList<>();
    public ImageView[][] tokens = new ImageView[8][8];
    Button btnCol1 , btnCol2 ,btnCol3 ,btnCol4 ,btnCol5 ,btnCol6 ,btnCol7 ,btnCol8 ;
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_game);
        btnCol1 = findViewById(R.id.column1);
        btnCol2 = findViewById(R.id.column2);
        btnCol3 = findViewById(R.id.column3);
        btnCol4 = findViewById(R.id.column4);
        btnCol5 = findViewById(R.id.column5);
        btnCol6 = findViewById(R.id.column6);
        btnCol7 = findViewById(R.id.column7);
        btnCol8 = findViewById(R.id.column8);
        btnCol1.setClickable(true);
        btnCol2.setClickable(true);
        btnCol3.setClickable(true);
        btnCol4.setClickable(true);
        btnCol5.setClickable(true);
        btnCol6.setClickable(true);
        btnCol7.setClickable(true);
        btnCol8.setClickable(true);

        GridLayout g = findViewById(R.id.grid);

        TextView turn = findViewById(R.id.turnText);
        turn.setTextColor(getResources().getColor(R.color.colorPrimaryDark));
        float sp = ((4 * getResources().getDisplayMetrics().density)) ;
        for(int i = 0 ; i < 8 ; i ++){
            for(int j = 0 ; j < 8 ; j ++){
             tokens[i][j] = new ImageView(this);
             tokens[i][j].setImageResource(R.drawable.wdot);
             GridLayout.LayoutParams param =new GridLayout.LayoutParams();
             if(i==0) param.topMargin = (int)sp;
             else param.topMargin = 0;
             if(j == 0 ) param.leftMargin = (int)sp;
             if(j == 0 ) param.leftMargin = (int)sp;
             else param.leftMargin = 0;
             param.rightMargin = Math.round(sp*2) ;
             param.bottomMargin = Math.round(sp*2) ;
             param.columnSpec = GridLayout.spec(j);
             param.rowSpec = GridLayout.spec(i);
             tokens[i][j].setLayoutParams(param);
             g.addView(tokens[i][j]);
            }
        }
        for(int i = 0 ; i < 8 ; i ++){
            gameArray.add(new ArrayList<String>());
        }
        btnCol1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                gameClick(1);
            }
        });
        btnCol2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                gameClick(2);
            }
        });
        btnCol3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                gameClick(3);
            }
        });
        btnCol4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                gameClick(4);
            }
        });
        btnCol5.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                gameClick(5);
            }
        });
        btnCol6.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                gameClick(6);
            }
        });
        btnCol7.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                gameClick(7);
            }
        });
        btnCol8.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                gameClick(8);
            }
        });
    }
    public void gameClick(int c ){

        if(p1Turn){
            if(gameArray.get(c-1).size() < 8) {
                gameArray.get(c - 1).add("1");
                tokens[8-gameArray.get(c-1).size()][c-1].setImageResource(R.drawable.rdot);
                TextView turn = findViewById(R.id.turnText);
                turn.setTextColor(getResources().getColor(R.color.colorPrimary));
                turn.setText(R.string.connect_four_Player2);
                if(isTie(gameArray)){
                    turn.setText(R.string.connect_four_Tie);
                }
                if(GameWon(toArray(gameArray) , "1")){
                    turn.setTextColor(getResources().getColor(R.color.colorPrimaryDark));
                    turn.setText(R.string.connect_four_Player1W);
                    stop();
                }
                p1Turn = false;
            }
        }
        else {
            if(gameArray.get(c-1).size() < 8) {
                gameArray.get(c - 1).add("2");
                tokens[8-gameArray.get(c-1).size()][c-1].setImageResource(R.drawable.ydot);
                TextView turn = findViewById(R.id.turnText);
                turn.setTextColor(getResources().getColor(R.color.colorPrimaryDark));
                turn.setText(R.string.connect_four_Player1);
                if(isTie(gameArray)){
                    turn.setText(R.string.connect_four_Tie);
                }
                if(GameWon(toArray(gameArray) , "2")){
                    turn.setTextColor(getResources().getColor(R.color.colorPrimary));
                    turn.setText(R.string.connect_four_Player2W);
                    stop();
                }
                p1Turn = true;
            }
        }

    }
    public String[][] toArray(ArrayList<ArrayList<String>> array){
        String[][] output = new String[8][8];
        for(int i = 0 ; i < 8 ; i ++){
            for(int j = 0 ; j < 8 ; j ++) {
                output[i][j] = "0";
            }
        }
        for(int i = 0 ; i < 8 ; i ++){
            for(int j = 0 ; j < array.get(i).size() ; j ++) {
                output[7-j][i] = array.get(i).get(j);
            }
        }
        return output;
    }
    public static boolean GameWon(String[][] intBoard ,String s) {
        for (int r = 0; r < intBoard.length - 3; r++) {
            for (int c = 0; c < intBoard[0].length - 3; c++) {
                if ((intBoard[r][c].equals(s)
                        && intBoard[r + 1][c + 1].equals(s)
                        && intBoard[r + 2][c + 2].equals(s)
                        && intBoard[r + 3][c + 3].equals(s) )
                ){
                    return true;
                }
            }
        }

        for (int r = 0; r < intBoard.length - 3; r++) {
            for (int c = 0; c < intBoard[0].length; c++) {
                if ( (intBoard[r][c].equals(s)
                        && intBoard[r + 1][c].equals(s)
                        && intBoard[r + 2][c].equals(s)
                        && intBoard[r + 3][c].equals(s))

                ) {
                    return true;
                }
            }
        }

        for (int r = 0; r < intBoard.length; r++) {
            for (int c = 0; c < intBoard[0].length - 3; c++) {
                if (intBoard[r][c].equals(s)
                        && intBoard[r][c + 1].equals(s)
                        && intBoard[r][c + 2].equals(s)
                        && intBoard[r][c + 3].equals(s)) {
                    return true;
                }
            }
        }

        for (int r = 3; r < intBoard.length; r++) {
            for (int c = 0; c < intBoard[0].length - 3; c++) {
                if (intBoard[r][c].equals(s)
                        && intBoard[r - 1][c + 1].equals(s)
                        && intBoard[r - 2][c + 2].equals(s)
                        && intBoard[r - 3][c + 3].equals(s)) {
                    return true;
                }
            }
        }
        return false;
    }
    public void stop(){
        btnCol1.setClickable(false);
        btnCol2.setClickable(false);
        btnCol3.setClickable(false);
        btnCol4.setClickable(false);
        btnCol5.setClickable(false);
        btnCol6.setClickable(false);
        btnCol7.setClickable(false);
        btnCol8.setClickable(false);

    }
    public boolean isTie(ArrayList<ArrayList<String>> array){
        for(int i = 0 ; i < 8 ; i ++){
            if(array.get(i).size() < 8)
                return false;
        }
        return true;
    }
    public void reset(View view){
        Intent I = getIntent();
        finish();
        startActivity(I);
    }
    public void goHome(View view){
        this.finish();
    }
}
