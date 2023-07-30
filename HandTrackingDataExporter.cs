using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

public class HandTrackingDataExporter : MonoBehaviour
{
    public OVRSkeleton skeleton;
    public bool isRightHand;
    public string customFolderPath; // Custom folder path to save the data

    private string csvFilePath;
    private StreamWriter csvWriter;

    // Start is called before the first frame update
    void Start()
    {
        // Create the custom folder if it doesn't exist
        if (!Directory.Exists(customFolderPath))
            Directory.CreateDirectory(customFolderPath);

        // Create a CSV file to save the data
        string timestamp = System.DateTime.Now.ToString("yyyyMMdd_HHmmss");
        csvFilePath = Path.Combine(customFolderPath, "HandTrackingData_" + timestamp + ".csv");
        csvWriter = new StreamWriter(csvFilePath, true);

        // Write headers to the CSV file
        csvWriter.WriteLine("Timestamp, Joint, PositionX, PositionY, PositionZ, RotationX, RotationY, RotationZ, RotationW");
    }

    // Update is called once per frame
    void Update()
    {
        // Get hand bone data from the OVRSkeleton
        List<OVRBone> handBones = new List<OVRBone>(skeleton.Bones);

        // Write data to the CSV file
        string timestamp = Time.time.ToString("F3");
        foreach (OVRBone bone in handBones)
        {
            string joint = bone.Id.ToString();
            string position = string.Format("{0:F6},{1:F6},{2:F6}", bone.Transform.position.x, bone.Transform.position.y, bone.Transform.position.z);
            string rotation = string.Format("{0:F6},{1:F6},{2:F6},{3:F6}", bone.Transform.rotation.x, bone.Transform.rotation.y, bone.Transform.rotation.z, bone.Transform.rotation.w);
            string dataEntry = string.Format("{0},{1},{2},{3}", timestamp, joint, position, rotation);
            csvWriter.WriteLine(dataEntry);
        }
    }

    // Called when the application is closed
    private void OnApplicationQuit()
    {
        // Close the CSV writer
        if (csvWriter != null)
        {
            csvWriter.Flush();
            csvWriter.Close();
        }
    }
}
