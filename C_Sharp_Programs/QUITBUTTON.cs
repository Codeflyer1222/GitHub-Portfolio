using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BUTTON : MonoBehaviour
{
    public void Quiting()
    {
        Debug.Log ("QUIT");

        Application.Quit();
    }
}
