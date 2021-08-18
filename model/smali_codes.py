

class SmaliCodes:
    """
    Class Smalicodes

        To Hold all smali code that needed for Apk Logger
    """
    package_name = "com/ramdurgasai/ApkLogger"


    log_method = """
    #################################      Apk Logger (Logging Method)    #############################
    const-string v0 ,"log_string"

    invoke-static {v0},Lcom/ramdurgasai/ApkLogger/logging;->printToLogcatandTextFile(Ljava/lang/String;)V
    ####################################################################################################
    """

    smali_file = """.class public com/ramdurgasai/ApkLogger/logging;
.super Ljava/lang/Object;
.source "logging.java"


# direct methods
.method public constructor <init>()V
    .registers 1

    .prologue
    .line 10
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static getMethodName()Ljava/lang/String;
    .registers 3

    .prologue
    .line 107
    new-instance v1, Ljava/lang/Throwable;

    invoke-direct {v1}, Ljava/lang/Throwable;-><init>()V

    .line 108
    invoke-virtual {v1}, Ljava/lang/Throwable;->getStackTrace()[Ljava/lang/StackTraceElement;

    move-result-object v1

    const/4 v2, 0x0

    aget-object v1, v1, v2

    .line 109
    invoke-virtual {v1}, Ljava/lang/StackTraceElement;->getMethodName()Ljava/lang/String;

    move-result-object v0

    .line 111
    .local v0, "nameofCurrMethod":Ljava/lang/String;
    return-object v0
.end method

.method public static hi()V
    .registers 0

    .prologue
    .line 129
    return-void
.end method

.method public static methodNameToTextFile()V
    .registers 5
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/io/IOException;
        }
    .end annotation

    .prologue
    .line 115
    const-string v2, "sdcard/ApkLogger_logs.txt"

    .line 116
    .local v2, "textFilepath":Ljava/lang/String;
    new-instance v3, Ljava/lang/Throwable;

    invoke-direct {v3}, Ljava/lang/Throwable;-><init>()V

    .line 117
    invoke-virtual {v3}, Ljava/lang/Throwable;->getStackTrace()[Ljava/lang/StackTraceElement;

    move-result-object v3

    const/4 v4, 0x0

    aget-object v3, v3, v4

    .line 118
    invoke-virtual {v3}, Ljava/lang/StackTraceElement;->getMethodName()Ljava/lang/String;

    move-result-object v0

    .line 120
    .local v0, "nameofCurrMethod":Ljava/lang/String;
    new-instance v1, Ljava/io/FileWriter;

    new-instance v3, Ljava/io/File;

    invoke-direct {v3, v2}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    invoke-direct {v1, v3}, Ljava/io/FileWriter;-><init>(Ljava/io/File;)V

    .line 121
    .local v1, "strwrt":Ljava/io/FileWriter;
    const-string v3, "Invoked Method "

    invoke-virtual {v1, v3}, Ljava/io/FileWriter;->write(Ljava/lang/String;)V

    .line 122
    invoke-virtual {v1}, Ljava/io/FileWriter;->close()V

    .line 125
    return-void
.end method

.method public static print(Ljava/lang/String;)V
    .registers 1
    .param p0, "string"    # Ljava/lang/String;

    .prologue
    .line 14
    invoke-static {p0}, com/ramdurgasai/ApkLogger;->printToLog(Ljava/lang/String;)I

    .line 15
    return-void
.end method

.method public static print(Ljava/lang/String;B)V
    .registers 4
    .param p0, "str"    # Ljava/lang/String;
    .param p1, "i"    # B

    .prologue
    .line 26
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-static {p1}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, com/ramdurgasai/ApkLogger;->printToLog(Ljava/lang/String;)I

    return-void
.end method

.method public static print(Ljava/lang/String;C)V
    .registers 4
    .param p0, "str"    # Ljava/lang/String;
    .param p1, "i"    # C

    .prologue
    .line 27
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-static {p1}, Ljava/lang/String;->valueOf(C)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, com/ramdurgasai/ApkLogger;->printToLog(Ljava/lang/String;)I

    return-void
.end method

.method public static print(Ljava/lang/String;I)V
    .registers 4
    .param p0, "str"    # Ljava/lang/String;
    .param p1, "i"    # I

    .prologue
    .line 23
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-static {p1}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, com/ramdurgasai/ApkLogger;->printToLog(Ljava/lang/String;)I

    return-void
.end method

.method public static print(Ljava/lang/String;Ljava/lang/Boolean;)V
    .registers 4
    .param p0, "str"    # Ljava/lang/String;
    .param p1, "i"    # Ljava/lang/Boolean;

    .prologue
    .line 30
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, com/ramdurgasai/ApkLogger;->printToLog(Ljava/lang/String;)I

    return-void
.end method

.method public static print(Ljava/lang/String;Ljava/lang/Double;)V
    .registers 4
    .param p0, "str"    # Ljava/lang/String;
    .param p1, "i"    # Ljava/lang/Double;

    .prologue
    .line 29
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, com/ramdurgasai/ApkLogger;->printToLog(Ljava/lang/String;)I

    return-void
.end method

.method public static print(Ljava/lang/String;Ljava/lang/Float;)V
    .registers 4
    .param p0, "str"    # Ljava/lang/String;
    .param p1, "i"    # Ljava/lang/Float;

    .prologue
    .line 28
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, com/ramdurgasai/ApkLogger;->printToLog(Ljava/lang/String;)I

    return-void
.end method

.method public static print(Ljava/lang/String;Ljava/lang/Long;)V
    .registers 4
    .param p0, "str"    # Ljava/lang/String;
    .param p1, "i"    # Ljava/lang/Long;

    .prologue
    .line 25
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, com/ramdurgasai/ApkLogger;->printToLog(Ljava/lang/String;)I

    return-void
.end method

.method public static print(Ljava/lang/String;Ljava/lang/Object;)V
    .registers 5
    .param p0, "str"    # Ljava/lang/String;
    .param p1, "object"    # Ljava/lang/Object;

    .prologue
    .line 57
    :try_start_0
    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    .line 58
    invoke-static {p0}, com/ramdurgasai/ApkLogger;->printToLog(Ljava/lang/String;)I

    .line 59
    invoke-static {p0}, com/ramdurgasai/ApkLogger;->printToTextFile(Ljava/lang/String;)V
    :try_end_1b
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_1b} :catch_1c

    .line 62
    :goto_1b
    return-void

    .line 61
    :catch_1c
    move-exception v0

    .local v0, "e":Ljava/lang/Exception;
    goto :goto_1b
.end method

.method public static print(Ljava/lang/String;Ljava/lang/String;)V
    .registers 3
    .param p0, "string"    # Ljava/lang/String;
    .param p1, "string1"    # Ljava/lang/String;

    .prologue
    .line 17
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, com/ramdurgasai/ApkLogger;->printToLog(Ljava/lang/String;)I

    .line 18
    return-void
.end method

.method public static print(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
    .registers 4
    .param p0, "string"    # Ljava/lang/String;
    .param p1, "string1"    # Ljava/lang/String;
    .param p2, "string2"    # Ljava/lang/String;

    .prologue
    .line 20
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, com/ramdurgasai/ApkLogger;->printToLog(Ljava/lang/String;)I

    .line 21
    return-void
.end method

.method public static print(Ljava/lang/String;Ljava/util/ArrayList;)V
    .registers 5
    .param p0, "str"    # Ljava/lang/String;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Ljava/lang/String;",
            "Ljava/util/ArrayList",
            "<",
            "Ljava/lang/Object;",
            ">;)V"
        }
    .end annotation

    .prologue
    .line 49
    .local p1, "arrayList":Ljava/util/ArrayList;, "Ljava/util/ArrayList<Ljava/lang/Object;>;"
    :try_start_0
    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v1, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, com/ramdurgasai/ApkLogger;->printToLog(Ljava/lang/String;)I
    :try_end_18
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_18} :catch_19

    .line 52
    :goto_18
    return-void

    .line 50
    :catch_19
    move-exception v0

    .local v0, "e":Ljava/lang/Exception;
    goto :goto_18
.end method

.method public static print(Ljava/lang/String;Ljava/util/HashMap;)V
    .registers 4
    .param p0, "str"    # Ljava/lang/String;
    .param p1, "hashMap"    # Ljava/util/HashMap;

    .prologue
    .line 34
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {p1}, Ljava/util/HashMap;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, com/ramdurgasai/ApkLogger;->printToLog(Ljava/lang/String;)I

    .line 35
    return-void
.end method

.method public static print(Ljava/lang/String;Ljava/util/HashMap;Ljava/util/HashMap;)V
    .registers 5
    .param p0, "str"    # Ljava/lang/String;
    .param p1, "hashMap"    # Ljava/util/HashMap;
    .param p2, "hashMap1"    # Ljava/util/HashMap;

    .prologue
    .line 37
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {p1}, Ljava/util/HashMap;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {p2}, Ljava/util/HashMap;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, com/ramdurgasai/ApkLogger;->printToLog(Ljava/lang/String;)I

    .line 38
    return-void
.end method

.method public static print(Ljava/lang/String;S)V
    .registers 4
    .param p0, "str"    # Ljava/lang/String;
    .param p1, "i"    # S

    .prologue
    .line 24
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-static {p1}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, com/ramdurgasai/ApkLogger;->printToLog(Ljava/lang/String;)I

    return-void
.end method

.method public static print(Ljava/util/ArrayList;)V
    .registers 2
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Ljava/util/ArrayList",
            "<",
            "Ljava/lang/String;",
            ">;)V"
        }
    .end annotation

    .prologue
    .line 45
    .local p0, "arrayList":Ljava/util/ArrayList;, "Ljava/util/ArrayList<Ljava/lang/String;>;"
    invoke-virtual {p0}, Ljava/util/ArrayList;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, com/ramdurgasai/ApkLogger;->printToLog(Ljava/lang/String;)I

    .line 46
    return-void
.end method

.method public static print(Ljava/util/HashMap;)V
    .registers 2
    .param p0, "hashMap"    # Ljava/util/HashMap;

    .prologue
    .line 40
    invoke-virtual {p0}, Ljava/util/HashMap;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, com/ramdurgasai/ApkLogger;->printToLog(Ljava/lang/String;)I

    .line 41
    return-void
.end method

.method public static printToLog(Ljava/lang/String;)I
    .registers 2
    .param p0, "string"    # Ljava/lang/String;

    .prologue
    .line 100
    const-string v0, "$xyz "

    invoke-static {v0, p0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    move-result v0

    return v0
.end method

.method public static printToLogcatandTextFile(Ljava/lang/String;)V
    .registers 2
    .param p0, "log"    # Ljava/lang/String;

    .prologue
    .line 82
    :try_start_0
    invoke-static {p0}, com/ramdurgasai/ApkLogger;->printToTextFile(Ljava/lang/String;)V

    .line 83
    invoke-static {p0}, com/ramdurgasai/ApkLogger;->print(Ljava/lang/String;)V
    :try_end_6
    .catch Ljava/io/IOException; {:try_start_0 .. :try_end_6} :catch_7

    .line 89
    :goto_6
    return-void

    .line 85
    :catch_7
    move-exception v0

    goto :goto_6
.end method

.method public static printToTextFile(Ljava/lang/String;)V
    .registers 4
    .param p0, "str"    # Ljava/lang/String;
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/io/IOException;
        }
    .end annotation

    .prologue
    .line 93
    const-string v1, "sdcard/ApkLogger_logs.txt"

    .line 94
    .local v1, "textFilepath":Ljava/lang/String;
    new-instance v0, Ljava/io/FileWriter;

    new-instance v2, Ljava/io/File;

    invoke-direct {v2, v1}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    invoke-direct {v0, v2}, Ljava/io/FileWriter;-><init>(Ljava/io/File;)V

    .line 95
    .local v0, "strwrt":Ljava/io/FileWriter;
    invoke-virtual {v0, p0}, Ljava/io/FileWriter;->write(Ljava/lang/String;)V

    .line 96
    invoke-virtual {v0}, Ljava/io/FileWriter;->close()V

    .line 98
    return-void
.end method


    """