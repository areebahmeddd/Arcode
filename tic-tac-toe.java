package Arcode;

import java.util.Scanner;
import java.util.Arrays;

class TicTacToe {
    static Scanner input = new Scanner(System.in);
    static String player;
    static String[] board = new String[9];

    public static void main(String[] args) {
        startGame();
        startGameLoop();
    }

    // Initializes the game, prompts the user to choose a player and sets up the game board
    private static void startGame() {
        System.out.println("=> Welcome to 3x3 Tic-Tac-Toe!");
        System.out.print("Choose player (X or O): ");
        player = input.nextLine().toUpperCase();

        initializeGameBoard();
        displayGameBoard();
        System.out.print("Enter slot number for " + player + ": ");
    }

    // Sets up the game board with slot numbers representing available moves
    private static void initializeGameBoard() {
        for (int i = 0; i < board.length; i++) {
            board[i] = String.valueOf(i + 1);
        }
    }

    // Displays the game board in a 3x3 grid format
    private static void displayGameBoard() {
        System.out.println("\n +-----------+");
        System.out.println(" | " + board[0] + " | " + board[1] + " | " + board[2] + " |");
        System.out.println(" |-----------|");
        System.out.println(" | " + board[3] + " | " + board[4] + " | " + board[5] + " |");
        System.out.println(" |-----------|");
        System.out.println(" | " + board[6] + " | " + board[7] + " | " + board[8] + " |");
        System.out.println(" +-----------+\n");
    }

    // Handles player moves and determines the game result
    private static void startGameLoop() {
        String result = null;

        while (result == null) {
            int slot = input.nextInt();

            if (slot > 0 && slot <= 9) {
                if (board[slot - 1].equals(String.valueOf(slot))) {
                    board[slot - 1] = player;

                    if (player.equals("X")) {
                        player = "O";
                    } else {
                        player = "X";
                    }

                    displayGameBoard();
                    result = checkGameResult();
                } else {
                    System.out.print("\n [Slot Taken] Re-enter slot number: ");
                }
            } else {
                System.out.print("\n [Invalid Input] Re-enter slot number: ");
            }
        }

        if (result.equals("Draw")) {
            System.out.println("=> It's a draw!");
        } else {
            System.out.println("=> Congratulations, " + result + " has won!");
        }
    }

    // Checks the game board for a winner or a draw and returns the result
    private static String checkGameResult() {
        String[] winningCombination = {
            board[0] + board[1] + board[2],
            board[3] + board[4] + board[5],
            board[6] + board[7] + board[8],
            board[0] + board[3] + board[6],
            board[1] + board[4] + board[7],
            board[2] + board[5] + board[8],
            board[0] + board[4] + board[8],
            board[2] + board[4] + board[6]
        };

        for (String line : winningCombination) {
            if (line.equals("XXX")) {
                return "X";
            } else if (line.equals("OOO")) {
                return "O";
            }
        }

        for (int i = 0; i < 9; i++) {
            if (Arrays.asList(board).contains(String.valueOf(i + 1))) {
                break;
            } else if (i == 8) {
                return "Draw";
            }
        }

        System.out.print("Enter slot number for " + player + ": ");
        return null;
    }
}