package khaled.alaya.jwt_demo.model;

import java.time.LocalDate;
import java.util.List;

import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.JoinTable;
import jakarta.persistence.ManyToMany;
import jakarta.persistence.OneToMany;
import jakarta.persistence.Table;

@Table(name = "chat")
@Entity
public class chat {


    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    Long id;
    String chatTitle;
    LocalDate created_at;
    LocalDate update_at;
    
    @ManyToMany
    @JoinTable(
        name = "chat_users",
        joinColumns = @JoinColumn(name = "chat_id"),
        inverseJoinColumns = @JoinColumn(name = "user_id")
    )
    List<user> user_id;


    @OneToMany(fetch = FetchType.LAZY, mappedBy = "chat_id")
    List<message> messages;



    public chat(){

    }

    public chat(String chatTitle){
        this.chatTitle=chatTitle;
        created_at=LocalDate.now();
        update_at=LocalDate.now();
    }

    
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getChatTitle() {
        return chatTitle;
    }

    public void setChatTitle(String chatTitle) {
        this.chatTitle = chatTitle;
    }

    public LocalDate getCreated_at() {
        return created_at;
    }

    public void setCreated_at(LocalDate created_at) {
        this.created_at = created_at;
    }

    public LocalDate getUpdate_at() {
        return update_at;
    }

    public void setUpdate_at(LocalDate update_at) {
        this.update_at = update_at;
    }

    public List<message> getMessages() {
        return messages;
    }

    public void setMessages(List<message> messages) {
        this.messages = messages;
    }
    
    public List<user> getUser_id() {
        return user_id;
    }

    public void setUser_id(List<user> user_id) {
        this.user_id = user_id;
    }
    @Override
    public String toString() {
        return "chat [id=" + id + ", chatTitle=" + chatTitle + ", created_at=" + created_at + ", update_at=" + update_at
                + ", user_id=" + user_id + ", messages=" + messages + "]";
    }



    
    
}
