package khaled.alaya.jwt_demo.model;

import java.time.LocalDate;

import com.fasterxml.jackson.annotation.JsonIgnore;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Table(name = "message")
@Entity
public class message {


    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id ;
    private String content;
    private LocalDate created_at;

    @ManyToOne
    @JsonIgnore
    private chat chat_id;
    @ManyToOne
    private user user_id;

    public message(){

    }
    public message(String content){
        this.content=content;
        this.created_at=LocalDate.now();
    }
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getContent() {
        return content;
    }
    public void setContent(String content) {
        this.content = content;
    }
    public LocalDate getCreated_at() {
        return created_at;
    }
    public void setCreated_at(LocalDate created_at) {
        this.created_at = created_at;
    }
    public chat getChat_id() {
        return chat_id;
    }
    public void setChat_id(chat chat_id) {
        this.chat_id = chat_id;
    }
    public user getUser_id() {
        return user_id;
    }
    public void setUser_id(user user_id) {
        this.user_id = user_id;
    }
    @Override
    public String toString() {
        return "message [id=" + id + ", content=" + content + ", created_at=" + created_at + ", chat_id=" + chat_id;
    }

    
}
