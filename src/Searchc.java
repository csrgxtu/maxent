//*******************************************************************
// Author: Archer Reilly
// Date: 14/Aug/2014
// File: Searchc.java
// Des: this class used to load file into string and then search a
//  phrase
//
// Produced By CSRGXTU
//*******************************************************************

import java.io.File;
import java.io.FileNotFoundException;
import java.nio.charset.Charset;
import java.io.IOException;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Searchc {
  /**
   * content is the string version of the file
   */
  private String content = null;
  
  private String fileName = null;
  
  /**
   * fileHD is the file handler
   */
  private File fileHD = null;
  
  
  /**
   * Constructor, initialize the mem variable.
   *
   * @param String fileName
   * @throws IllegalArgumentException
   */
  public Searchc(String fileName) {
    if (fileName == null) {
      throw new IllegalArgumentException("FileSaver:Constructor parameter"
        + " Not set correctly!");
    }
    
    this.fileName = fileName;

    try {
      this.content = readFile(fileName, Charset.defaultCharset());
    } catch (IOException e) {
      System.out.println("an exception");
    }
  }

  /**
   * readFile
   * read file into string
   *
   * @param path (String)
   * @param encoding (Charset)
   * @return String
   */
  public String readFile(String path, Charset encoding) throws IOException {
    byte[] encoded = Files.readAllBytes(Paths.get(path));
    return new String(encoded, encoding);
  }

  /**
   * hasPhrase
   * check if the file content has the phrase you give
   *
   * @param phrase (String)
   * @return boolean
   */
  public boolean hasPhrase(String phrase) {
    if (phrase == "" || phrase == null) {
      return false;
    }

    String pattern = ".*(" + phrase + ").*";
    Pattern r = Pattern.compile(pattern);

    Matcher m = r.matcher(this.content);
    if (m.find()) {
      //System.out.println("Found value: "  + m.group(0));
      return true;
    } else {
      //System.out.println("Not Found");
      return false;
    }
  }

  /**
   * hasPhrasea
   * use contains method of the string search a phrase
   *
   * @param phrase (String)
   * @return boolean
   */
  public boolean hasPhrasea(String phrase) {
    if (phrase == "" || phrase == null) {
      return false;
    }

    if (this.content.contains(phrase)) {
      //System.out.println("Found value: "  + phrase);
      return true;
    } else {
      //System.out.println("Not Found");
      return false;
    }
  }
  
  public String getContent() {
    return this.content;
  }
  
  public String getFileName() {
    return this.fileName;
  }
  
  public void setContent(String content) {
    this.content = content;
  }
  
  public void setFileName(String fileName) {
    this.fileName = fileName;
  }

  public static void main(String[] args) {
    Searchc s = new Searchc("data.txt");
    System.out.println(s.getContent());
    s.hasPhrase("岳阳");
    s.hasPhrasea("岳阳");
  }
}
