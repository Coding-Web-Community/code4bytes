package com.craftxbox.main;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.TimeZone;

public class Main {

	public static void main(String[] args) {
		//yyyy-mm-dd HH:mm:ss - yyyy-mm-dd HH:mm:ss

		try {
			File input = new File("time.log");
			BufferedReader reader = new BufferedReader(new FileReader(input));
			StringBuilder stringBuilder = new StringBuilder();
			String line = null;
			String ls = System.getProperty("line.separator");
			while ((line = reader.readLine()) != null) {
				stringBuilder.append(line);
				stringBuilder.append(ls);
			}
			stringBuilder.deleteCharAt(stringBuilder.length() - 1);
			reader.close();
			String content = stringBuilder.toString();
			String[] lines = content.split("\n");
			SimpleDateFormat inputFormatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
			inputFormatter.setTimeZone(TimeZone.getTimeZone("UTC"));
			SimpleDateFormat outputFormatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
			outputFormatter.setTimeZone(TimeZone.getTimeZone("UTC"));
			Map<String,Long> lengths = new HashMap<>();
			long total = 0;
			long highest = 0;
			String highestID = "";
			long lowest = 1700000000000l;
			String lowestID = "";
			for(String i : lines) {
				String times = i.split("\\|")[0];
				String[] split = times.split(" - ");
				try {
					long beginningDate = inputFormatter.parse(split[0].trim()).getTime();
					long endDate = inputFormatter.parse(split[1].trim()).getTime();
					String id = i.split("\\|")[1].trim();
					long delta = endDate-beginningDate;
					lengths.put(id,delta);
					total+=delta;
					if(delta > highest) {
						highest = delta;
						highestID = id;
					}
					if(delta < lowest) {
						lowest = delta;
						lowestID = id;
					}
				} catch (ParseException e) {
					e.printStackTrace();
				}
			}
			long average = total/lines.length;
			String currentClosest = "";
			long currentClosestDelta = 1700000000000l;
			for(Entry<String,Long> i : lengths.entrySet()) {
				long delta = i.getValue() - average;
				if(delta < 0) {
					delta *= -1;
				}
				if(delta < currentClosestDelta) {
					currentClosestDelta = delta;
					currentClosest = i.getKey();
				}
			}
			System.out.println("Sessions:"+lines.length);
			System.out.println("Total  Δ:"+outputFormatter.format(new Date(total)));
			System.out.println("HighestΔ:"+highestID+" "+highest);
			System.out.println("Lowest Δ:"+lowestID+" "+lowest);
			System.out.println("AverageΔ:"+total/lines.length);
			System.out.println("ClosestΔ:"+currentClosest);
		} catch (IOException e1) {
			e1.printStackTrace();
		}

	}



}
