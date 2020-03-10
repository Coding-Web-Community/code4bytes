//written by blackware

public static void main(String[] args) {
        //launch(args);

        int[] arr ={7, 6, 8, 5, 7, 4, 6, 5, 5, 6, 4, 5, 5, 6, 6, 7, 5, 8, 6, 7, 7, 6, 6, 5, 5, 6, 4, 5, 3, 6, 2};
        List<Integer> lel = new ArrayList<>();

        for(int i = 1; i <= arr.length-2;i++){
            int ervoor = arr[i-1];
            int midden = arr[i];
            int erna = arr[i+1];

            if (erna < midden && ervoor < midden){
                lel.add(i);
            }
        }
        System.out.println(lel);

    }
