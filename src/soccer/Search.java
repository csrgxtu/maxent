/**
 * Author: Archer Reilly
 * Date: 14/Aug/2014
 * File: Search.java
 * Description: this class is used to search a phrase in a text file
 * Website: http://csrgxtu.blog.com
 *
 * Produced By CSRGXTU
 */

public class Search {
  /**
   * absPath is the absolute path to the file
   */
  public String absPath = null;

  Scanner sc = null;

  public void Search(String absPath) {
    self.absPath = absPath;
    self.sc = new Scanner(new File(absPath));
  }

  public boolean hasPhrase(String phrase) {
    if (self.sc.
  }

  public String getAbsPath() {
    return self.absPath;
  }

  public void setAbsPath(String absPath) {
    self.absPath = absPath;
  }
}
