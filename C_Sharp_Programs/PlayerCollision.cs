using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class PlayerCollision : MonoBehaviour
{
    public Movement movement;
    //specail thing made by unity that works the same as start and update
    void OnCollisionEnter (Collision CollisionInfo)
    {
        if(CollisionInfo.collider.tag == "Obstacle")
       {
        movement.enabled = false;
        FindObjectOfType<GameManager>().EndgGame();

       }
    }
}
