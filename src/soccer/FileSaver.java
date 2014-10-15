//*******************************************************************
// Author: Archer Reilly
// Date: 18/Mar/2014
// File: FileSaver.java
// Des: this class is used to save a string into file on the disk,
//  nothing else
//
// Produced By CSRGXTU
//*******************************************************************

import java.io.File;
import java.io.PrintWriter;
import java.io.FileNotFoundException;

public class FileSaver {
  /**
   * content is the content string that gonna to be saved into the
   * file.
   */
  private String content = null;
  
  /**
   * fileName is the file name that will be placed on the disk
   */
  private String fileName = null;
  
  /**
   * fileHD is the file handler
   */
  private File fileHD = null;
  
  
  /**
   * Constructor, initialize the mem variable.
   *
   * @param String
   * @param String
   */
  public FileSaver(String content, String fileName) {
    // check out the parameter
    if (content == null || fileName == null) {
      throw new IllegalArgumentException("FileSaver:Constructor parameter"
        + " Not set correctly!");
    }
    
    this.setContent(content);
    this.setFileName(fileName);
    
    this.fileHD = new File(this.getFileName());
  }
  
  /**
   * save, save the content into the file
   *
   * @return boolean
   */
  public boolean save() {
    /*if (!this.canSave()) {
      // debugging
      System.out.println("what the fuck");
      return false;
    }*/
    
    try {
      PrintWriter output = new PrintWriter(this.fileHD);
      
      output.print(this.getContent());
      
      output.close();
      
      return true;
    } catch (FileNotFoundException e) {
      return false;
    }
  }
  
  /**
   * canSave, helper method, check the conditions before saving het file.
   *
   * @return boolean
   */
  private boolean canSave() {
    // if file already exist, can not save
    if (this.fileHD.exists()) {
      return false;
    }
    
    // can be written?
    if (!this.fileHD.canWrite()) {
      return false;
    }
    
    // is directory?
    if (this.fileHD.isDirectory()) {
      return false;
    }
    
    // all is ok
    return true;
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
  
  // testing
  /*public static void main(String[] args) {
    String fileName = "../data/test.txt";
    String content = "what the fuck, it is awsome!";
    
    FileSaver fileSaver = new FileSaver(content, fileName);
    if (fileSaver.save()) {
      System.out.println("Succed!");
    } else {
      System.out.println("Failed!");
    }
    //System.out.println(fileSaver.getFileName());
  }*/
}
