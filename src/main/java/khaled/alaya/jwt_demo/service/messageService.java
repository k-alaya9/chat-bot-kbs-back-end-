package khaled.alaya.jwt_demo.service;

import java.util.List;

import org.springframework.stereotype.Service;

import khaled.alaya.jwt_demo.model.chat;
import khaled.alaya.jwt_demo.model.message;
import khaled.alaya.jwt_demo.model.messageRequest;
import khaled.alaya.jwt_demo.repo.chatRepo;
import khaled.alaya.jwt_demo.repo.messageRepo;
import khaled.alaya.jwt_demo.repo.userRepo;

@Service
public class messageService {

    private messageRepo messageRepo;
    private chatRepo chatRepo;
    private userRepo userRepo;
    public messageService(khaled.alaya.jwt_demo.repo.messageRepo messageRepo,chatRepo chatRepo,userRepo userRepo) {
        this.messageRepo = messageRepo;
        this.chatRepo=chatRepo;
        this.userRepo=userRepo;
    }


    public message addMessage(messageRequest newMessage,String user){
        message newMsg=new message(newMessage.content());
        newMsg.setChat_id(chatRepo.findById(newMessage.chat_id()).get());
        newMsg.setUser_id(userRepo.findByusername(user).get());
        // System.out.println(newMsg);
        return messageRepo.save(newMsg);
    }

    public List<message> findByChat_id(Long chat){
       chat messages=chatRepo.findById(chat).get();
        return messageRepo.findmessageByChat(messages);
    }


    public void deleteMessage(message deletedMessage){
        messageRepo.delete(deletedMessage);
    }

}
